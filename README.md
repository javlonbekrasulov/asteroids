# Asteroids
 
A classic Asteroids arcade game built with Python and Pygame.
 
---
 
## Demo
 
> ![Gameplay](assets/asteroids-gameplay.mp4)
 
---
 
## Features
 
- Classic Asteroids arcade gameplay
- Asteroids split into smaller pieces when shot
- Shooting cooldown mechanic
- Game over when an asteroid collides with the player
- Randomized asteroid field generation
---
 
## Controls
 
| Key | Action |
|-----|--------|
| `W` | Thrust forward |
| `A` | Rotate left |
| `D` | Rotate right |
| `Spacebar` | Shoot |
 
---
 
## Installation
 
**Prerequisites:** Python 3.13+
 
1. Clone the repository:
   ```bash
   git clone https://github.com/javlonbekrasulov/asteroids.git
   cd asteroids
   ```
 
2. Install dependencies:
   ```bash
   pip install pygame
   ```
 
3. Run the game: 
it is recommended to use [uv](https://github.com/astral-sh/uv):
```bash
uv run main.py
```