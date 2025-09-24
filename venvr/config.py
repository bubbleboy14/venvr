from fyg import Config

config = Config({
	"port":{
		"slice": 10,
		"block": 100,
		"start": 17000
	},
	"vstore": "venvrs",
	"startwait": 2
})

def getPortBlock():
	pcfg = config.port
	start = pcfg.start
	pcfg.update("start", pcfg.start + pcfg.block)
	return start