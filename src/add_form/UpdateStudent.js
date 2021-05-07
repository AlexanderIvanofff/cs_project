import React from "react";
import {observer} from "mobx-react";
import {observable} from "mobx";

@observer
class UpdateStudent extends React.Component {
    @observable showForm = false;
    @observable courses = null;
    @observable student = null;

    render() {
        return (
            <div>
                <button onClick={(e) => {
                    fetch("/show_all_courses", {
                        method: "POST", // or 'PUT'
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({}),
                    })
                        .then(response => response.json())
                        .then(courses => {
                            console.log("Success:22222", courses);
                            this.courses = courses;

                            fetch("/show_all_Students_and_there_courses", {
                                method: "POST", // or 'PUT'
                                headers: {
                                    "Content-Type": "application/json",
                                },
                                body: JSON.stringify({}),
                            })
                                .then(response => response.json())
                                .then(student => {
                                    console.log("Success:22222", student);
                                    this.student = student;
                                    this.showForm = !this.showForm;
                                })
                                .catch((error) => {
                                    console.error("Error:", error);
                                });
                        })
                        .catch((error) => {
                            console.error("Error:", error);
                        });

                }}>{this.showForm ? "hide": "show"}
                </button>
                {this.showForm &&
                <form
                    onSubmit={(event) => {
                        event.preventDefault();
                        this.props.updateStudent({
                            course_id: this.course_id.value, student_id: this.student_id.value
                        });
                        this.showForm = false;
                    }}>

                    <select id="CourseId" ref={(ref) => {
                        this.student_id = ref;
                    }}>
                        {this.student.show_all_Students_and_there_courses.map(student => {
                            return <option key={student[1]} value={student[0]}>{student[1]} {student[2]} </option>
                        })}
                    </select>


                    <select id="CourseId" ref={(ref) => {
                        this.course_id = ref;
                    }}>
                        {this.courses.show_all_courses.map(course => {
                            return <option key={course[1]} value={course[0]}>{course[1]}</option>
                        })}
                    </select>
                    <button type={"submit"}>Update Student</button>
                </form>}
            </div>
        );
    }
}

export default UpdateStudent;