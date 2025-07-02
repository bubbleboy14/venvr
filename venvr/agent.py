from os.path import isdir, join as pjoin
from fyg import Config
from fyg.util import Named
from .runner import Runner
from .builder import Builder

class Agent(Named):
	def __init__(self, name, vstore, deps=[], persistent=True, port=None):
		self.name = name
		if persistent:
			self.log("adding dez dependency for persistent mode")
			deps.append("dez")
		self.config = Config({
			"deps": deps,
			"running": {},
			"registered": {},
			"nextport": port,
			"vstore": vstore,
			"persistent": persistent
		})
		self.setup()

	def getport(self):
		cfg = self.config
		if not cfg.persistent:
			return
		np = cfg.nextport
		cfg.update("nextport", cfg.nextport + 1)
		self.log("getport", np)
		return np

	def start(self, fname):
		cfg = self.config
		port = cfg.registered[fname]
		self.log("starting", fname, port)
		cfg.running.update(fname, True)
		self.runner.start(fname, port)

	def run(self, fname, *args, **kwargs):
		self.log("run", fname, args, kwargs)
		if self.config.persistent and not self.config.running[fname]:
			self.start(fname)
		return self.runner.run(fname, *args, **kwargs)

	def register(self, func):
		port = self.getport()
		name = self.builder.register(func, port)
		self.log("registered", name, port)
		self.config.registered.update(name, port)
		return name

	def setup(self):
		self.log("setup")
		self.setpaths()
		self.runner = Runner(self.name, self.config)
		self.builder = Builder(self.name, self.config)
		isdir(self.config.path.base) or self.builder.build()

	def setpaths(self):
		base = pjoin(self.config.vstore, self.name)
		self.log("setpaths", base)
		venv = pjoin(base, "venv")
		binp = pjoin(venv, "bin")
		self.config.update("path", {
			"base": base,
			"venv": venv,
			"pip": pjoin(binp, "pip"),
			"py": pjoin(binp, "python"),
			"run": {}
		})