import random
import pygame

class Particle():
     
    def __init__(self, pos=(0, 0), size=15, life=1000, color=(0, 255, 0), shape="square"):
        self.pos = pos
        self.size = size
        self.color = pygame.Color(color)
        self.age = 0 # in miliseconds
        self.life = life
        self.dead = False
        #include shape parameter to enable additional shapes
        self.shape = shape
        self.alpha = 255
        self.surface = self.update_surface()

    def update(self, dt):
        self.age += dt
        if self.age > self.life:
            self.dead = True
        self.alpha = 255 * (1 - (self.age / self.life))
        

    def update_surface(self):
        size = int(self.size)

        surf = pygame.Surface((int(size * 0.8), int(size * 0.8)), pygame.SRCALPHA)

        if self.shape == "square":
            pygame.draw.rect(surf, self.color, (0, 0, size, size))

        elif self.shape == "circle":
            pygame.draw.circle(surf, self.color, (size//2, size//2), size//2)


        return surf
        
    def draw(self, surface):
        self.surface.set_alpha(self.alpha)
        surface.blit(self.surface, self.pos)


class ParticleTrail():

    def __init__(self, pos, size, life, color, shapes):

        shapes = ["square", "circle"]
        particle = Particle
        self.pos = pos
        self.size = size
        self.life = life
        #pass color into particle trail
        self.color = color
        self.shapes = shapes
        self.particles = []
        

    def update(self, dt):
        #update color of particle
        particle = Particle(self.pos, size=self.size, life=self.life, color=self.color,
        shape=random.choice(self.shapes))
        self.particles.insert(0, particle)
        self._update_particles(dt)
        self._update_pos()


    def _update_particles(self, dt):
        for idx, particle in enumerate(self.particles):
            particle.update(dt)
            if particle.dead:
                del self.particles[idx]


    def _update_pos(self):
        x, y = self.pos
        y += self.size
        self.pos = (x, y)

    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)


class Rain():

    def __init__(self, screen_res):
        self.screen_res = screen_res
        self.particle_size = 15
        self.birth_rate = 1
        self.trails = []

    def update(self, dt):
        self._birth_new_trails()
        for idx, trail in enumerate(self.trails):
            trail.update(dt)
            if self._trail_is_offscreen(trail):
                del self.trails[idx]


    def _trail_is_offscreen(self, trail):
    # If there are no particles, consider the trail offscreen
        if not trail.particles:
            return True
        tail_is_offscreen = trail.particles[-1].pos[1] > self.screen_res[1]
        return tail_is_offscreen
    

    def _birth_new_trails(self):
        for count in range(self.birth_rate):
            screen_Wdith = self.screen_res[0]
            x = random.randrange(0, screen_Wdith, self.particle_size)
            pos = (x, 0)
            life = random.randrange(500, 3000)
            #import color index
            color = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
            ]
            #color of the trails alternate
            shapes = ["square", "circle"]
            color = random.choice(color)
            trail = ParticleTrail(pos, self.particle_size, life, color, shapes)
            self.trails.insert(0, trail)


    def draw(self, surface):
        for trail in self.trails:
            trail.draw(surface)

    
        
def main():
        pygame.init()
        pygame.display.set_caption("Digital Rain")
        clock = pygame.time.Clock()
        dt = 0    
        resolution = (1920, 1080)
        screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
        rain = Rain(resolution)
        running = True
        while running: 
            #Event Loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                #create if statement that changes background color
                #background color changed via user input
                #elif statement for different background colors tied to different input

            #Render and display stuff
            rain.update(dt)
            #background color variable
            bg_color = pygame.Color(0, 0, 0)
            screen.fill(bg_color)
            rain.draw(screen)
            pygame.display.flip()
            dt = clock.tick(12)
        pygame.quit()

if __name__ == "__main__":
    main()