class position:
	"""
	N
	E
	U
	R
	A
	L

	N
	E
	T
	W
	O
	R
	K
	S
	"""
	
	def __init__(self):
		self.holdings = {}
		self.priceList = {}
		self.lastUpdated = {}

	def buy(self, src, dst, amount):
		"""
		B
		U
		Y

		L
		O
		W
		"""
		#src is currency used to buy dst currency
		#Could change assert to if else (returning NoneType) if conditions not met
		assert src in self.holdings, "No holdings in this source currency"
		assert dst + ":" + src in priceList, "Src:Dst currency pairing does not exist"
		assert self.holdings[src] >= amount, "Insufficient holdings in source currency"
		################################################################################
		self.holdings[src] -= amount
		if dst not in self.holdings:
			self.holdings[dst] = 0
		self.holdings[dst] += (1 / self.priceList[dst + ":" + src]) * amount

	def sell(self, src, dst, amount):
		"""
		S
		E
		L
		L

		H
		I
		G
		H
		"""
		#src currency being sold for dst currency
		#eg. I sell 5 Eth (src) for USD (dst)
		assert src in self.holdings, "No holdings in this source currency"
		assert src + ":" + dst in priceList, "Src:Dst currency pairing does not exist"
		assert self.holdings[src] >= amount, "Insufficient holdings in source currency"
		self.holdings[src] -= amount
		if dst not in self.holdings:
			self.holdings[dst] = 0
		self.holdings[dst] += self.priceList[dst + ":" + src] * amount



