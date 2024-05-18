export default function updateStudentGradeByCity(
  getListStudents,
  city,
  newGrades,
) {
  if (!Array.isArray(getListStudents)) {
    return [];
  }
  return getListStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.filter(
        (grade) => grade.studentID === student.id,
      )[0];
      return {
        ...student,
        grade: grade ? grade.grade : 'N/A',
      };
    });
}
