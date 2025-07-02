from .manager import Manager

manny = None

def getman():
	global manny
	if not manny:
		manny = Manager()
	return manny

def getagent(name, deps=[], persistent=True):
	return getman().agent(name, deps, persistent)

def run(envname, deps, func, *args, **kwargs):
	agent = getagent(envname, deps)
	return agent.run(agent.register(func), *args, **kwargs)