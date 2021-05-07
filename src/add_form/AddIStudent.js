import React from "react";
import {observer} from "mobx-react";
import {observable} from "mobx";

@observer
class AddIStudent extends React.Component {
    @observable showForm = false;
    @observable courses = null;

    render() {
        return (
            <div>
                <button onClick={(e) => {
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
                                this.showForm = !this.showForm;
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
                        if (!(this.first_name.value && this.last_name.value)) {
                            alert("Need first & last names & courses!!!")
                            return false
                        }
                        this.props.addStudent({
                            first_name: this.first_name.value,
                            last_name: this.last_name.value,
                            course_id: this.course_id.value
                        });
                        this.first_name.value -= "";
                        this.last_name.value = "";
                    }}>

                    <input
                        placeholder={"First Name"}
                        ref={(ref) => {
                            this.first_name = ref;
                        }}
                    />
                    <input
                        placeholder={"Last Name"}
                        ref={(ref) => {
                            this.last_name = ref;
                        }}
                    />

                    <select id="CourseId" ref={(ref) => {
                        this.course_id = ref;
                    }}>
                        {this.courses.show_all_courses.map(course => {
                            return <option key={course[1]} value={course[0]}>{course[1]}</option>
                        })}
                    </select>
                    <button type={"submit"}>Add Student</button>
                </form>}
            </div>
        );
    }
}

export default AddIStudent;