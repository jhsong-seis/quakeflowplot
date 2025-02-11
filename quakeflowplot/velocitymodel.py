import pandas as pd
import matplotlib.pyplot as plt


def grad_to_layer(vel):
    '''
    vel: Pandas.DataFrame
    columns: z_km, vp, vs
    '''
    z_km, vp, vs = [], [], []
    for i in range(len(vel) - 1):
        z_km.append(vel.iloc[i]['z_km'])
        z_km.append(vel.iloc[i+1]['z_km'])
        vp.append(vel.iloc[i]['vp'])
        vp.append(vel.iloc[i]['vp'])
        vs.append(vel.iloc[i]['vs'])
        vs.append(vel.iloc[i]['vs'])
    z_km.append(vel.iloc[-1]['z_km'])
    vp.append(vel.iloc[-1]['vp'])
    vs.append(vel.iloc[-1]['vs'])
    return pd.DataFrame({'z_km':z_km, 'vp':vp, 'vs':vs}, columns=vel.columns)

def plot_vel_1d(vel):
    '''
    vel: Pandas.DataFrame
    columns: z_km, vp, vs
    '''
    fig, ax = plt.subplots(figsize=(4, 6))
    ax.plot(vel['vp'], vel['z_km'], 'b-', label='Vp')
    ax.plot(vel['vs'], vel['z_km'], 'r-', label='Vs')
    # ax.invert_yaxis()
    ax.set_ylim(vel['z_km'].max(), vel['z_km'].min())
    ax.set_title('1D Velocity Model')
    ax.set_xlabel('Velocity (km/s)')
    ax.set_ylabel('Depth (km)')
    ax.legend(loc='upper right')
    fig.tight_layout()
    return fig