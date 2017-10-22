from django.shortcuts import render
import json
from .models import Currents, Trap
import pandas as pd
import numpy as np

def index(request):
    data = pd.DataFrame.from_records(
        Currents.objects.values('density',
                                    'current', 'time', 'forceMean', 'forceStd'))
    means = pd.DataFrame.from_records(Currents.objects.values('forceMean','forceStd'))
    meanVals = means['forceMean'].unique().tolist()
    meanVars = means['forceStd'].unique().tolist()
    displayMean = request.POST.get("mean",0)
    displayStd = request.POST.get("std", 0.5)
    data = data.query('(forceMean == {}) & (forceStd == " {}")'.format(displayMean,displayStd))
    data['velocity'] = data['current'].astype(float) * data['density'].astype(float)/(data['time'] * 1000)
    currents = data.groupby('density', as_index=False).mean()[['density','velocity']]

    velocities = currents['velocity'].values.tolist()
    velocities.insert(0, 'mean = {}, std = {}'. format(displayMean, displayStd))

    velocities = json.dumps(velocities)

    densities = currents['density'].values.tolist()
    densities.insert(0, 'x')

    densities = json.dumps(densities)
    jasonTest = currents.to_json(orient='records')

    means = meanVals
    means = json.dumps(means)
    std = meanVars
    std = json.dumps(std)
    return render(request, 'motors/index.html',
            {'data': jasonTest, 'velocities': velocities, 'densities': densities,
            'means': means, 'std': std})

def singleMotor(request):
    data = pd.DataFrame.from_records(
        Trap.objects.values('event', 'dwell', 'force')
    )
    data['event'] = data['event'].str.strip()
    forwardSteps = data.query('event == "Forward"').head(1000)
    backSteps = data.query('event == "Backward"').head(1000)
    detachments = data.query('event == "Detach"').head(1000)

    stepCounts = data.groupby(['force','event']).count()['dwell'].reset_index()
    forwardCount = stepCounts.query('event =="Forward"')
    backCount = stepCounts.query('event == "Backward"')
    detachCount = stepCounts.query('event == "Detach"')
    bdCount = backCount.set_index('force').join(detachCount.set_index('force'), how='outer', lsuffix='_back', rsuffix='_detach')
    bdCount['dwell'] = bdCount['dwell_back'] + bdCount['dwell_detach']
    ratios = forwardCount.set_index('force').join(
                        backCount.set_index('force'),
                        how = 'outer',
                        lsuffix = '_forward',
                        rsuffix = '_back'
    )
    ratios2 = forwardCount.set_index('force').join(
                        bdCount['dwell'].to_frame(),
                        how = 'outer',
                        lsuffix = '_forward',
                        rsuffix = '_back'
    )
    ratios['ratio'] = ratios['dwell_forward'].astype(float) / ratios['dwell_back']
    ratios2['ratio'] = ratios2['dwell_forward'].astype(float) / ratios2['dwell_back']

    ratios = ratios2['ratio'].dropna()
    ratioForce = ratios.index.tolist()
    ratioForce.insert(0, 'ratioForce')
    ratioValue = ratios.values.tolist()
    ratioValue.insert(0, 'ratioValue')

    forwardDwells = forwardSteps.dwell.tolist()
    forwardDwells.insert(0, 'forwardDwell')
    forwardForce = forwardSteps.force.tolist()
    forwardForce.insert(0, 'forwardForce')
    backDwells = backSteps.dwell.tolist()
    backDwells.insert(0, 'backDwell')
    backForce = backSteps.force.tolist()
    backForce.insert(0, 'backForce')
    detachDwell = detachments.dwell.tolist()
    detachDwell.insert(0, 'detachDwell')
    detachForce = detachments.force.tolist()
    detachForce.insert(0, 'detachForce')

    return render(request, 'motors/single.html',
            {'forwardDwells': json.dumps(forwardDwells), 'forwardForce':json.dumps(forwardForce),
             'backDwells':json.dumps(backDwells), 'backForce':json.dumps(backForce),
             'detachDwells':json.dumps(detachDwell), 'detachForce':json.dumps(detachForce),
             'ratioForce':ratioForce, 'ratioValue': ratioValue})


# Create your views here.
