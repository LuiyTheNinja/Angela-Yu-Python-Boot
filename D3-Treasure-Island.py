print(r"""
                              *            .        *
                    .                  .         .
          .                .                     .

                            ___
                      _____/___\_____
                 ____/_______________\____
                /_________________________\
               |  _     _     _     _      |
               | |_|   |_|   |_|   |_|     |
               |                           |
          _____|___________________________|_____
         /_______________________________________\
                 \___/               \___/

                      ISS WAYFARER - SCV-117

     Beyond the edge of charted space, where no signals travel
     and no stars bear names, your vessel drifts alone...
""")

print("""
╔══════════════════════════════════════════════════════════════╗
║                    STARSIM: DRIFTPOINT                      ║
║                    Deep Space Expedition                    ║
╚══════════════════════════════════════════════════════════════╝

Year 2479.

Humanity's frontier lies thousands of light-years behind you.

Your salvage vessel, the ISS Wayfarer, drifts silently through
an uncharted sector beyond mapped space. No trade routes.
No colonies. No distress beacons.

Only darkness.

Three days ago, long-range scanners detected something impossible:
a massive artificial structure of unknown origin orbiting a dead star.

No transponder.
No known design signatures.
No records.

Just a solitary monument drifting through eternity.

You are the first person to ever lay eyes upon it.

As your airlock cycles open, the pale glow of your helmet lamp
cuts through centuries of darkness.

Ahead stands a colossal wall of black metallic alloy stretching
beyond sight in both directions.

Ancient symbols pulse faintly beneath its surface.

For the first time in your career, you feel truly alone.

Mission Objectives:
► Investigate the structure
► Locate the source of the energy readings
► Survive

""")

intro_choice = input("""
Your scanner shows two possible routes:

[PORT]       Follow a maintenance trench running along the structure.
[STARBOARD]  Move toward a collapsed docking section.

Choose PORT or STARBOARD:
""").upper()

if intro_choice == "PORT":

    path_choice = input("""
Several hundred meters ahead, the trench ends at a breach
in the structure's outer hull.

Your scanner detects unstable power fluctuations nearby.

Do you:

[BREACH] Enter through the opening.

or

[SCAN] Perform a detailed systems scan first.

Choose BREACH or SCAN:
""").upper()

    if path_choice == "SCAN":

        print("""
You deploy an autonomous survey drone.

Several minutes pass.

The drone returns with a partial map of the interior.

A hidden maintenance shaft leads upward toward the strongest
energy signature detected within the structure.

You begin the ascent.
""")

        door_choice = input("""
After a difficult climb, you emerge into a vast chamber.

Four ancient access doors stand before you.

Above each doorway glows a colored symbol:

[RED]
[BLUE]
[YELLOW]
[WHITE]

Choose a door:
""").upper()

        if door_choice == "RED":

            print("""
The door seals shut behind you.

Emergency lights activate.

WARNING: Plasma Containment Breach.

The chamber erupts into a ball of superheated energy.

You are vaporized instantly.

MISSION FAILED
""")

        elif door_choice == "BLUE":

            print("""
Darkness.

Your helmet lamp flickers.

Motion sensors begin reporting movement.

Something is here.

Before you can react, a massive shape emerges from the shadows.

Your transmission cuts off abruptly.

MISSION FAILED
""")

        elif door_choice == "WHITE":

            print("""
The floor suddenly disappears beneath you.

Hull integrity failure detected.

Explosive decompression tears through the chamber.

You are launched into the endless void.

No rescue signal is ever received.

MISSION FAILED
""")

        elif door_choice == "YELLOW":

            print("""
The ancient door groans open.

Beyond lies a corridor illuminated by golden energy conduits.

At its end rests a crystalline artifact unlike anything
humanity has ever discovered.

Its light fills the chamber.

You have located the legendary Driftpoint Core.

MISSION SUCCESS

TREASURE FOUND
""")

        else:
            print("""
Unable to decide, you remain in the chamber too long.

Life support systems begin failing.

Eventually, your oxygen supply runs dry.

MISSION FAILED
""")

    else:

        print("""
Ignoring your scanner's warning, you enter the breach.

The floor collapses beneath your feet.

You plunge into an abandoned reactor chamber.

Toxic coolant floods the compartment.

Your suit fails within seconds.

MISSION FAILED
""")

else:

    print("""
You head toward the collapsed docking section.

Ancient metal groans beneath your feet.

Without warning, centuries-old support structures fail.

Thousands of tons of alloy collapse around you.

Your expedition ends before it truly begins.

MISSION FAILED
""")

print("""
═══════════════════════════════════════════════════════════════
                  THANK YOU FOR PLAYING
                       STARSIM: DRIFTPOINT
═══════════════════════════════════════════════════════════════
""")