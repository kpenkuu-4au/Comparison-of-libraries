import matplotlib.pyplot as plt


def rotation_3d(ax):
    if ax:
        for angle in range(0, 360 * 4 + 1):
            angle_norm = (angle + 180) % 360 - 180
            rotation1 = rotation2 = rotation3 = 0
            if angle <= 360:
                rotation1 = angle_norm
            elif angle <= 360 * 2:
                plt.axis('off')
                rotation2 = angle_norm
            elif angle <= 360 * 3:
                plt.axis('on')
                rotation3 = angle_norm
            else:
                plt.axis('off')
                rotation1 = rotation2 = rotation3 = angle_norm
            ax.view_init(rotation1, rotation2, rotation3)
            plt.draw()
            plt.pause(.001)
    else:
        raise TypeError('Object is not axis')
