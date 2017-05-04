from Clase.Alumno import Alumno
from Clase.Materia import Materia

UnAlumno=Alumno()
UnAlumno.setNombre("Allahu")
UnAlumno.setApellido("Akbar")
UnAlumno.setFecha(2017, 3, 17)

M=Materia()
M.setNombre("Matematica")
M.ListaNotas=[1, 2]
UnAlumno.setMaterias(M)
M.agregarNota(8)
M.agregarNota(9)

Ma=Materia()
Ma.setNombre("Castellano")
UnAlumno.setMaterias(Ma)
Ma.agregarNota(10)
Ma.agregarNota(7)

print(UnAlumno.promedioMinimo())
print(UnAlumno.promedioNotasAlumno())
print(UnAlumno.promedioMaximo())
print(UnAlumno.mayorNota("Matematica"))
print(UnAlumno.menorNota("Matematica"))
print(UnAlumno.mayorNota("Castellano"))
print(UnAlumno.menorNota("Castellano"))






