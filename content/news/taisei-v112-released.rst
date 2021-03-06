Taisei v1.1.2 Released!
#######################
:date: 2017-11-20 07:27
:author: Taisei team
:slug: taisei-v112-released

This is a maintenance release of the stable v1.1 branch. It doesn't have any gameplay changes, and consists entirely of bugfixes and improvements backported from the v1.2 development tree.

.. raw:: html

   </p>

Replays recorded with v1.1 and v1.1.1 should be fully compatible with this version, and vice versa.

.. raw:: html

   </p>

Some of the notable changes are:

.. raw:: html

   </p>

-  

   .. raw:: html

      </p>

   Fixed sound not working with SDL_mixer 2.0.2 due to incorrect initialization

   order.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Made all audio resources optional. Taisei will no longer abort when trying to

   load music or a sound effect when the audio subsystem has failed to initialize

   or was disabled at build time.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Fixed various issues related to fullscreen and window management.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Implemented a more robust way to choose an appropriate SDL video driver. The

   ``TAISEI_VIDEO_DRIVER`` environment variable is now deprecated. See

   `here <https://github.com/taisei-project/taisei/blob/v1.1.2/ENVIRON.md#video-and-opengl>`__

   for details.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   On Windows systems with hybrid graphics (typically laptops), Taisei will now

   attempt to use the more powerful discrete GPU by default.

   .. raw:: html

      </p>

-  

   .. raw:: html

      </p>

   Fixed a linking error that occured for dynamically linked Windows builds. The

   official releases for Windows are still statically linked, however.

   .. raw:: html

      </p>

.. raw:: html

   </p>

Go grab it from the `Download <https://taisei-project.org/download>`__ section.

.. raw:: html

   </p>
