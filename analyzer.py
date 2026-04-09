def analyze_code(code):
	issues = []

	if "calc(" in code:
		issues.append("Bad function name")

	return issues
