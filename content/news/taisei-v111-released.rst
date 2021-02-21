Taisei v1.1.1 Released!
#######################
:date: 2017-10-28 00:40
:author: Taisei team
:slug: taisei-v111-released

This is a maintenance release of the stable v1.1 branch. It doesn't have any gameplay changes, and consists entirely of bugfixes and improvements backported from the v1.2 development tree.

.. raw:: html

   </p>

Replays recorded with v1.1 should be fully compatible with this version, and vice versa.

.. raw:: html

   </p>

Some of the notable changes are:

.. raw:: html

   </p>

-  

   .. raw:: html

      </p>

   Vertical synchronization (vsync) is now disabled by default, as it causes

   percieved input latency for some players. If you'd like to use it and/or you

   have screen tearing problems, you should set it to "on" or "adaptive" in the

   video settings.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   The event/input processing system has been completely rewritten, and unicode

   text input now works correctly.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Reimplemented the framerate limiter. It's significantly more accurate now and

   attempts to compensate for sudden frametime spikes. This makes the game much

   more likely to run at exactly the intended speed (60 frames per second).

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   The character's Power is now also displayed as a numeric value, in addition to

   the stars bar.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Fixed an unpleasant artifact in the boss background shader.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Fixed the "letterboxing" artifacts on some systems on non-4:3 resolutions.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Updated the SDL game controller database. More gamepads are supported

   out-of-the-box now.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Fixed the character getting stuck moving in some direction when using some

   gamepads in the "restricted" axes mode.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Fixed memory corruption that could occur when a gamepad has less axes than

   expected of an Xbox-like controller.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Fixed various build issues for Windows and macOS targets.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Updated the SDL version to 2.0.7 in the official Windows and macOS builds.

   .. raw:: html

      </p>

.. raw:: html

   </p>

Go grab it from the `Download <https://taisei-project.org/download>`__ section.

.. raw:: html

   </p>

As you can see, we are alive and well! v1.2 is under active development, with some pleasant surprises already present in the master branch *(SPOILERS:* *WE HAVE MUSIC)*.

.. raw:: html

   </p>
