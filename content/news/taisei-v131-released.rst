Taisei v1.3.1 Released!
#######################
:date: 2019-09-29 22:30
:author: Taisei team
:slug: taisei-v131-released

Hey, we are back for a little replay-compatible update to the 1.3 release. The changes include:

- **Improved laser rendering and other visual improvements**. The spell card opener looks yet a bit cooler, there are little indicators for off-screen items.

- **Player Spell Cards** now have proper names and declaration animations.

- **Optimizations** in various shaders that will make your toaster a bit happier about running Taisei. However, as usual, it is best if your toaster has good OpenGL drivers to avoid most trouble.

- The audio assets are now in **Opus** format, which reduces file size at increased fidelity. On that note, the file sizes in general have been reduced, which benefits the loading time of the web version of Taisei.

- Quite a few **bug fixes**. Of particular importance, two potentially game-breaking bugs have been vanquished:

   - In Cirno's very first spell “Perfect Freeze”, the player could (extremely rarely) get killed for no apparent reason. This was caused by a bug in bullet motion interpolation.

   - In some builds, MarisaA's lasers would render enemies permanently invulnerable, making them ineffective weapons to put it lightly.

But we actually have a big ace up our bullet riddled sleeves as well:

-  Complete replacement of the **character artwork** by `@afensorm <https://twitter.com/afensorm>`__.

They are cute, they are colorful and if you look carefully, some parts glow a bit. We also have some variable facial expressions incoming, but those will be part of version 1.4.

We are happy to also announce the new Switch homebrew port by `@p-sam <https://twitter.com/p__sam>`__. Now you can clear *Tower of Truth “Theory of Everything”* on public transport and impress your fellow passenger!

