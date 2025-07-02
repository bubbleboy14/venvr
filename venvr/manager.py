from fyg.util import Loggy
from .agent import Agent

class Manager(Loggy):
	def __init__(self, vstore):
		self.vstore = vstore
		self.venvrs = {} # detect?

	def subsig(self):
		return self.vstore

	def agent(self, name, deps=[], persistent=True):
		if name not in self.venvrs:
			self.log("delegating agent", name)
			self.venvrs[name] = Agent(name, self.vstore, deps, persistent)
		return self.venvrs[name]