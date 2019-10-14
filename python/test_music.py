from python.object_factory import *

# Escalas Mayores
# calculateScale(a_note, EQuality.Mayor)
# calculateScale(aS_note, EQuality.Mayor)
# calculateScale(b_note, EQuality.Mayor)
# calculateScale(c_note, EQuality.Mayor)
# calculateScale(cS_note, EQuality.Mayor)
# calculateScale(d_note, EQuality.Mayor)
# calculateScale(dS_note, EQuality.Mayor)
# calculateScale(e_note, EQuality.Mayor)
# calculateScale(f_note, EQuality.Mayor)
# calculateScale(fS_note, EQuality.Mayor)
# calculateScale(g_note, EQuality.Mayor)
# calculateScale(gS_note, EQuality.Mayor)
#
# # Escalas menores
# calculateScale(a_note, EQuality.Minor)
# calculateScale(aS_note, EQuality.Minor)
# calculateScale(b_note, EQuality.Minor)
# calculateScale(c_note, EQuality.Minor)
# calculateScale(cS_note, EQuality.Minor)
# calculateScale(d_note, EQuality.Minor)
# calculateScale(dS_note, EQuality.Minor)
# calculateScale(e_note, EQuality.Minor)
# calculateScale(f_note, EQuality.Minor)
# calculateScale(fS_note, EQuality.Minor)
# calculateScale(g_note, EQuality.Minor)
# calculateScale(gS_note, EQuality.Minor)

for scales_containing in findContainerScales(dm):
    scales_containing.printScaleName()

# Chord c = ObjectFactory.createChord(EQuality.Mayor, c_note, e_note, g_note);
# try:
#     #tone(15000,1000, 0.25);
#     #note()
#
# except Exception as e:
#     print("Error")

calculateScale(g_note, EQuality.Mayor)
