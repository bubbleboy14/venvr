from fyg.util import Loggy
from .agent import Agent
from .config import config, getPortBlock

class Manager(Loggy):
	def __init__(self, vstore=None):
		self.vstore = vstore or config.vstore
		self.nextPort = getPortBlock()
		self.venvrs = {} # detect?

	def subsig(self):
		return self.vstore

	def getport(self):
		np = self.nextPort
		pslice = config.port.slice
		self.log("assigning ports", np, "to", np + pslice - 1)
		self.nextPort += pslice
		return np

	def agent(self, name, deps=[], persistent=True):
		if name not in self.venvrs:
			self.log("delegating agent", name)
			self.venvrs[name] = Agent(name, self.vstore, deps,
				persistent, persistent and self.getport())
		return self.venvrs[name]