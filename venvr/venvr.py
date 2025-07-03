import sys
from optparse import OptionParser
from .manager import Manager
from .config import config

manny = None

def getman(vstore=None):
	global manny
	if not manny:
		manny = Manager(vstore)
	return manny

def getagent(name, deps=[], persistent=True):
	return getman().agent(name, deps, persistent)

def run(envname, deps, func, *args, **kwargs):
	agent = getagent(envname, deps)
	if type(func) is not str:
		func = agent.register(func)
	return agent.run(func, *args, **kwargs)

def call(envname, func, *args, **kwargs):
	return getagent(envname).run(func, *args, **kwargs)

def install(envname, pname):
	getagent(envname).builder.install(pname)

def profile(envname=None):
	(envname and getagent(envname) or getman()).profile()

def log(*msg):
	print("venvr", *msg)

def err(*msg):
	log("error!", *msg)
	sys.exit()

cli = {
	"call": call,
	"install": install,
	"profile": profile
}

def invoke():
	parser = OptionParser("venvr [call|install|profile] [env] [arg1] [arg2] ...")
	parser.add_option("-v", "--vstore", dest="vstore",
		default=config.vstore, help="where all the venvs live")
	options, args = parser.parse_args()
	if options.vstore != config.vstore:
		log("using vstore", options.vstore)
		config.update("vstore", options.vstore)
	args or err("what command?")
	cmd = args.pop(0)
	if cmd != "profile":
		args or err("what enviroment?")
	cli[cmd](*args)