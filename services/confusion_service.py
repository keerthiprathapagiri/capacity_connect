from datetime import datetime

def confusion_score(events):
 weights={'pause':1,'rewind':2,'replay':2,'seek_backward':2}
 return min(100,round(sum(weights.get(e.event_type,0) for e in events)*10,1))
def heatmap(events):
 out={}
 for e in events: out[int(e.timestamp or 0)]=out.get(int(e.timestamp or 0),0)+1
 return out
