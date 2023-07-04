score = {
'python': 80,
'django': 89,
'web': 83
}

score['algorithm'] = 90

score['python'] = 85

mean_score = (score['python'] + score['web'] + score['django'] + score['algorithm'])/4

print(mean_score)
