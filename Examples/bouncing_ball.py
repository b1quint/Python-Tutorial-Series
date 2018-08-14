#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Create an animation using classes
    and matplotlib.

    by B. Quint
"""

import matplotlib.pyplot as plt
import matplotlib.animation as pani

__all__ = ['main', 'Box', 'Particle']


def main():
    """
    Main method. Displays a window with two particles bouncing.
    """

    my_particle_1 = Particle(0.1, 0.001, 0.5, 0.000)
    my_particle_2 = Particle(0.2, 0.0025, 0.25, 0.003)
    my_particle_3 = Particle(0.3, 0.005, 0.1, 0.002)

    my_box = Box()
    my_box.add_particle(my_particle_1)
    my_box.add_particle(my_particle_2)
    my_box.add_particle(my_particle_3)

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    ax.set_xlim(0, 1), ax.set_xticks([])
    ax.set_ylim(0, 1), ax.set_yticks([])

    lines = []

    for p in my_box.list_of_particles:
        line, = ax.plot(p.x, p.y, 'o')
        lines.append(line)

    def update(frame_number):
        """
        Update the plot. Please, note that this function is defined
        **inside** the main function.
        """
        my_box.one_interaction()
        for i in range(my_box.n_particles):
            particle = my_box.list_of_particles[i]
            lines[i].set_data(particle.x, particle.y)

    animation = pani.FuncAnimation(fig, update, interval=10)
    plt.show()


class Box:

    def __init__(self):
        """Create one box to put particles"""
        self.xlimits = [0, 1]
        self.ylimits = [0, 1]
        self.list_of_particles = []
        self.n_particles = len(self.list_of_particles)

    def add_particle(self, particle):
        """Add one partice inside the box."""
        self.list_of_particles.append(particle)
        self.n_particles = len(self.list_of_particles)

    def one_interaction(self):
        """Update the position of the particle."""
        for p in self.list_of_particles:

            x_old = p.x
            y_old = p.y
            p.update()
            x_new = p.x
            y_new = p.y

            if p.x < min(self.xlimits):
                p.change_x_direction()
                p.x = min(self.xlimits) - (x_old - x_new)

            elif p.x > max(self.xlimits):
                p.change_x_direction()
                p.x = max(self.xlimits) - (x_new - x_old)

            if p.y < min(self.ylimits):
                p.change_y_direction()
                p.y = min(self.ylimits) - (y_old - y_new)

            elif p.y > max(self.ylimits):
                p.change_y_direction()
                p.y = max(self.ylimits) - (y_new - y_old)


class Particle:

    def __init__(self, x0, v0, y0, w0):
        """
        Creates a bouncing ball. To make this example
        clear, use x0 and y0 between 0 and 1 and v0 and w0 between 0.01
        and 0.1.

        Parameters
        ----------
            x0 : float
                Initial horizontal position.
            v0 : float
                Horizontal velocity.
            y0 : float
                Initial vertical position.
            w0 : float
                Vertical velocity.

        """
        self.x = x0
        self.y = y0
        self.v = v0
        self.w = w0

    def __str__(self):
        """This is a string representation."""
        return "[x, y] = [" \
               "{:03.2f}, {:03.2f}] - [v, w] = [{:03.2f}, {:03.2f}] - ".format(
                    self.x, self.y, self.v, self.w)

    def change_x_direction(self):
        """
        Change the direction of the particle in x.
        """
        self.v = -self.v

    def change_y_direction(self):
        """
        Change the direction of the particle in y.
        """
        self.w = -self.w

    def update(self):
        """
        Update the position where the particle is.
        """
        # Increment velocity
        self.x += self.v
        self.y += self.w


if __name__ == "__main__":
    main()
