import FreeCAD as App
import Part
import math

# Yeni bir doküman oluştur
doc = App.newDocument("AYS_Y1_Helical_Core")

# --- PARAMETRELER (mm cinsinden) ---
R_core = 300.0         # Çekirdek iç yarıçapı
H_core = 1200.0        # Aktif çekirdek yüksekliği
P = 1250.0             # Helis adımı (Pitch)
W_b = 45.0             # Basamak radyal genişliği
R_dump = 130.0         # Alt kuyu yarıçapı (D=260 mm)
H_dump = 600.0         # Alt kuyu derinliği
wall_th = 20.0         # Gövde et kalınlığı

# 1. DIŞ BASINÇ KABI VE ÇEKİRDEK BOŞLUĞU
outer_cyl = Part.makeCylinder(R_core + wall_th, H_core)
core_void = Part.makeCylinder(R_core, H_core)
vessel_shell = outer_cyl.cut(core_void)

# 2. ALT KRİTİK-ALTI ÇÖKME HAZNESİ (DUMP CHAMBER)
dump_outer = Part.makeCylinder(R_dump + wall_th, H_dump, App.Vector(0, 0, -H_dump))
dump_void = Part.makeCylinder(R_dump, H_dump, App.Vector(0, 0, -H_dump))
dump_shell = dump_outer.cut(dump_void)

# 3. HELİSEL BASAMAK RAMPA GEOMETRİSİ (SUGIHARA SPIRAL CASCADE)
helix_curve = Part.makeHelix(P, H_core, R_core, 0, False)

# Basamak en kesiti (45 mm genişlik, 20 mm et kalınlığı, 12 derece meyil)
p1 = App.Vector(R_core - W_b, 0, 0)
p2 = App.Vector(R_core, 0, 0)
p3 = App.Vector(R_core, 0, 20)
p4 = App.Vector(R_core - W_b, 0, 10)  # Akış meyil açısı
step_wire = Part.makePolygon([p1, p2, p3, p4, p1])
step_face = Part.Face(step_wire)

# Helis hattı boyunca katı süpürme
baffle_solid = step_face.makePipe(helix_curve)

# Parçaları birleştir
complete_core = vessel_shell.fuse(dump_shell).fuse(baffle_solid)

# FreeCAD arayüzüne nesneyi ekle
obj = doc.addObject("Part::Feature", "ReactorCore_Model1_1")
obj.Shape = complete_core
doc.recompute()
