import evaluate_rpe as ev

p1 = (1311878207.7766, -0.0403,-1.8042, 0.5784, -0.7472, -0.0219, 0.0319, 0.6634)
p2 =  (1311878208.2728, -0.0447, -1.6637, 0.5788, -0.7424, -0.0016, 0.0127, 0.6698)

a = ev.transform44( p1 )
b = ev.transform44( p2 )

r = ev.ominus( a,b)

print r
