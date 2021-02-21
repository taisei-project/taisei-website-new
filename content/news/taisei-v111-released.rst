Taisei v1.1.1 Released!
#######################
:date: 2017-10-28 00:40
:author: Taisei team
:slug: taisei-v111-released

This is a maintenance release of the stable v1.1 branch. It doesn't have any gameplay changes, and consists entirely of bugfixes and improvements backported from the v1.2 development tree.

Replays recorded with v1.1 should be fully compatible with this version, and vice versa.

Some of the notable changes are:

- Vertical synchronization (vsync) is now disabled by default, as it causes
  percieved input latency for some players. If you'd like to use it and/or you
  have screen tearing problems, you should set it to "on" or "adaptive" in the
  video settings.

- The event/input processing system has been completely rewritten, and unicode
  text input now works correctly.

- Reimplemented the framerate limiter. It's significantly more accurate now and
  attempts to compensate for sudden frametime spikes. This makes the game much
  more likely to run at exactly the intended speed (60 frames per second).

- The character's Power is now also displayed as a numeric value, in addition to
  the stars bar.

- Fixed an unpleasant artifact in the boss background shader.

- Fixed the "letterboxing" artifacts on some systems on non-4:3 resolutions.

- Updated the SDL game controller database. More gamepads are supported
   out-of-the-box now.

- Fixed the character getting stuck moving in some direction when using some
   gamepads in the "restricted" axes mode.

- Fixed memory corruption that could occur when a gamepad has less axes than
  expected of an Xbox-like controller.

- Fixed various build issues for Windows and macOS targets.

- Updated the SDL version to 2.0.7 in the official Windows and macOS builds.

Go grab it from the `Download <https://taisei-project.org/download>`__ section.

As you can see, we are alive and well! v1.2 is under active development, with some pleasant surprises already present in the master branch *(SPOILERS:* *WE HAVE MUSIC)*.

