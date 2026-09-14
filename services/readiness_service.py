def readiness_score(scores,threshold=60):
 vals=[float(x) for x in scores]; return round(sum(vals)/len(vals),1) if vals else 0
def is_ready(scores,threshold=60): return readiness_score(scores)>=threshold
