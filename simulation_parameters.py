def reset_the_simulation(
        self,
        *,
        seed: Optional[int] = None,
        return_info: bool = False,
        options: Optional[dict] = None,
):
    super().reset_the_simulation(seed=seed)
    self.state = self.np_random.uniform(low=-0.05, high=0.05, size=(4,))
    self.steps_beyond_done = None
    if not return_info:
        return np.array(self.state, dtype=np.float32)
    else:
        return np.array(self.state, dtype=np.float32), {}


def visualize_simulation(self, mode="human"):
    screen_width = 600
    screen_height = 400

    world_width = self.x_threshold * 2
    scale = screen_width / world_width
    polewidth = 10.0
    polelen = scale * (2 * self.length)
    cartwidth = 50.0
    cartheight = 30.0

    if self.state is None:
        return None

    x = self.state

    if self.screen is None:
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
    if self.clock is None:
        self.clock = pygame.time.Clock()

    self.surf = pygame.Surface((screen_width, screen_height))
    self.surf.fill((255, 255, 255))

    l, r, t, b = -cartwidth / 2, cartwidth / 2, cartheight / 2, -cartheight / 2
    axleoffset = cartheight / 4.0
    cartx = x[0] * scale + screen_width / 2.0  # MIDDLE OF CART
    carty = 100  # TOP OF CART
    cart_coords = [(l, b), (l, t), (r, t), (r, b)]
    cart_coords = [(c[0] + cartx, c[1] + carty) for c in cart_coords]
    gfxdraw.aapolygon(self.surf, cart_coords, (0, 0, 0))
    gfxdraw.filled_polygon(self.surf, cart_coords, (0, 0, 0))

    l, r, t, b = (
        -polewidth / 2,
        polewidth / 2,
        polelen - polewidth / 2,
        -polewidth / 2,
    )

    pole_coords = []
    for coord in [(l, b), (l, t), (r, t), (r, b)]:
        coord = pygame.math.Vector2(coord).rotate_rad(-x[2])
        coord = (coord[0] + cartx, coord[1] + carty + axleoffset)
        pole_coords.append(coord)
    gfxdraw.aapolygon(self.surf, pole_coords, (202, 152, 101))
    gfxdraw.filled_polygon(self.surf, pole_coords, (202, 152, 101))

    gfxdraw.aacircle(
        self.surf,
        int(cartx),
        int(carty + axleoffset),
        int(polewidth / 2),
        (129, 132, 203),
    )
    gfxdraw.filled_circle(
        self.surf,
        int(cartx),
        int(carty + axleoffset),
        int(polewidth / 2),
        (129, 132, 203),
    )

    gfxdraw.hline(self.surf, 0, screen_width, carty, (0, 0, 0))

    self.surf = pygame.transform.flip(self.surf, False, True)
    self.screen.blit(self.surf, (0, 0))
    if mode == "human":
        pygame.event.pump()
        self.clock.tick(self.metadata["render_fps"])
        pygame.display.flip()

    if mode == "rgb_array":
        return np.transpose(
            np.array(pygame.surfarray.pixels3d(self.screen)), axes=(1, 0, 2)
        )
    else:
        return self.isopen

def close_the_smimulation(self):
    if self.screen is not None:
        pygame.display.quit()
        pygame.quit()
        self.isopen = False
