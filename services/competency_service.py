def competency_score(assessment=0,teach_back=0,engagement=0): return round(min(100,assessment*.5+teach_back*.3+engagement*.2),1)
