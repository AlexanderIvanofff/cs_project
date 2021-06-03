import {hot} from "react-hot-loader";
import React from "react";
import "./App.less";
import {observer} from "mobx-react";
import {observable} from "mobx";
import AddIStudent from "./add_form/AddIStudent";
import Professors from "./main/Professors";
import AddProfessor from "./add_form/AddProfessor";
import UpdateStudent from "./add_form/UpdateStudent";
import AddCourse from "./add_form/AddCourse";
import Course from "./main/Course";
import Titles from "./main/Titles";
import AddTitle from "./add_form/AddTitle";
import ShowProfessorsAndCourses from "./main/ShowProfessorsAndCourses";
import ShowAllStudentsAndThereCourses from "./main/ShowAllStudentsAndThereCourses";
import ShowThreeTopCourses from "./main/ShowThreeTopCourses";
import ShowTopThreeProfessorsEnrolledStudents from "./main/ShowTopThreeProfessorsEnrolledStudents";


@observer
class App extends React.Component {
    // eslint-disable-next-line camelcase
    @observable current_data = null
    @observable professors = null
    @observable studentsAndCourses = null
    @observable showTopThreeCourses = null
    @observable courses = null
    @observable title = null
    @observable show_all_professors = null
    @observable show_top_three_professors_enrolled_students = null


    render() {
        return (
            <div className="App">
                <button onClick={() => {
                    this.getAllProfessorsAndCourses()
                }}>All Professors and Courses
                </button>
                <button onClick={() => {
                    this.getAllStudentsAndCourses()
                }}>All Students and Courses
                </button>
                <button onClick={() => {
                    this.getTopThreeCourses()
                }}>Top Three Courses
                </button>
                <button onClick={() => {
                    this.getAllCourses()
                }}>Load Courses
                </button>
                <button onClick={() => {
                    this.getAllTitles()
                }}>Load Titles
                </button>
                <button onClick={() => {
                    this.getAllProfessors()
                }}>Load Professors
                </button>
                <button onClick={() => {
                    this.getTopThreeProfessorsEnrolledStudents()
                }}>Load Top Three Professors
                </button>


                {this.professors !== null && <ShowProfessorsAndCourses professors={this.professors}/>}
                {this.studentsAndCourses !== null &&
                <ShowAllStudentsAndThereCourses studentsAndCourses={this.studentsAndCourses}
                                                delStudent={this.delStudent}/>}
                {this.showTopThreeCourses !== null &&
                <ShowThreeTopCourses showTopThreeCourses={this.showTopThreeCourses}/>}
                {this.show_top_three_professors_enrolled_students !== null && <ShowTopThreeProfessorsEnrolledStudents
                    show_top_three_professors_enrolled_students={this.show_top_three_professors_enrolled_students}/>}
                {this.courses !== null && <Course courses={this.courses} delCourse={this.deleteCourse}/>}
                {this.title !== null && <Titles title={this.title} delete_title={this.delTitle}/>}
                {this.show_all_professors !== null &&
                <Professors show_all_professors={this.show_all_professors} deleteProfessor={this.deleteProfessor}/>}


                <div className={"add-forms"}>
                    <div>
                        <h3>Add student</h3>
                        <AddIStudent addStudent={this.addStudent}/>
                    </div>
                    <div>
                        <h3>Add professors</h3>
                        <AddProfessor addProfessor={this.addProfessor}/>
                    </div>
                    <div>
                        <h3>Update student</h3>
                        <UpdateStudent updateStudent={this.updateStudent}/>
                    </div>
                    <div>
                        <h3>Add courses</h3>
                        <AddCourse addCourse={this.addCourse}/>
                    </div>
                    <div>
                        <h3>Add title</h3>
                        <AddTitle addTitle={this.addTitle}/>
                    </div>
                </div>
            </div>
        );
    }


    clearAllData = () => {
        this.professors = null;
        this.studentsAndCourses = null;
        this.showTopThreeCourses = null;
        this.courses = null;
        this.title = null;
        this.show_all_professors = null;
        this.show_top_three_professors_enrolled_students = null;
    }

    getAllProfessorsAndCourses() {
        this.clearAllData();
        const data = {};//this.current_data
        fetch("/show_all_professors_and_courses", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.professors = data;

            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

    getAllProfessors() {
        this.clearAllData();
        const data = {};//this.current_data
        fetch("/show_all_professors", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.show_all_professors = data;
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

    getAllStudentsAndCourses() {
        this.clearAllData();
        const data = {};//this.current_data
        fetch("/show_all_Students_and_there_courses", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.studentsAndCourses = data;
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

    getTopThreeCourses() {
        this.clearAllData();
        const data = {};//this.current_data
        fetch("/show_top_three_courses", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.showTopThreeCourses = data;
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

    getTopThreeProfessorsEnrolledStudents() {
        this.clearAllData();
        const data = {};//this.current_data
        fetch("/show_top_three_professors_enrolled_students_in_courses", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.show_top_three_professors_enrolled_students = data;
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

    getAllCourses() {
        this.clearAllData();
        const data = {};//this.current_data
        fetch("/show_all_courses", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.courses = data;
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

    getAllTitles() {
        this.clearAllData();
        const data = {};//this.current_data
        fetch("/show_all_titles", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.title = data;
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

    addStudent = (student) => {
        fetch("/add_student", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(student),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.current_data = null;

            })
            .catch((error) => {
                console.error("Error:", error);
            });

    }


    delStudent = (student) => {
        fetch("/delete_student", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: student,
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.current_data = null;
                this.getAllStudentsAndCourses()

            })
            .catch((error) => {
                console.error("Error:", error);
            });

    }

    updateStudent = (student) => {
        fetch("/update_student", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(student),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.current_data = null;

            })
            .catch((error) => {
                console.error("Error:", error);
            });

    }

    addProfessor = (professor) => {
        fetch("/add_professor", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(professor),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.current_data = null;

            })
            .catch((error) => {
                console.error("Error:", error);
            });

    }


    deleteProfessor = (professor) => {
        fetch("/delete_professor", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: professor,
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.current_data = null;
                this.getAllProfessors()
            })
            .catch((error) => {
                console.error("Error:", error);
            });

    }

    addCourse = (course) => {
        fetch("/add_course", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(course),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.courses = null;

            })
            .catch((error) => {
                console.error("Error:", error);
            });

    }

    deleteCourse = (course) => {
        fetch("/delete_course", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: course,
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.courses = null;
                this.getAllCourses()

            })
            .catch((error) => {
                console.error("Error:", error);
            });

    }


    addTitle = (title) => {
        fetch("/add_title", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(title),
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.current_data = null;
            })
            .catch((error) => {
                console.error("Error:", error);
            });

    }

    delTitle = (title) => {
        fetch("/delete_title", {
            method: "POST", // or 'PUT'
            headers: {
                "Content-Type": "application/json",
            },
            body: title,
        })
            .then(response => response.json())
            .then(data => {
                console.log("Success:22222", data);
                this.title = null;
                this.getAllTitles();

            })
            .catch((error) => {
                console.error("Error:", error);
            });
    }

}

export default hot(module)(App);