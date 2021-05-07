import React from "react";
import {observer} from "mobx-react";
import {observable} from "mobx";

@observer
class AddICourse extends React.Component {
    @observable showForm = false;
    @observable professor = null;

    render() {
        return (
            <div>
                <button onClick={(e) => {
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
                            this.professor = data;
                            this.showForm = !this.showForm;
                        })
                        .catch((error) => {
                            console.error("Error:", error);
                        });


                }}>Show Add Course
                </button>
                {this.showForm &&
                <form
                    onSubmit={(event) => {
                        event.preventDefault();
                        if (!(this.title.value && this.credits.value)) {
                            alert("Need title & credits & professor name!!!")
                            return false
                        }
                        this.props.addCourse({
                            title: this.title.value,
                            credits: this.credits.value,
                            professor_id: this.professor_id.value
                        });
                        this.first_name.value = "";
                        this.last_name.value = "";
                    }}>

                    <input
                        placeholder={"Title"}
                        ref={(ref) => {
                            this.title = ref;

                        }}
                    />

                    <input
                        placeholder={"Credits"}
                        ref={(ref) => {
                            this.credits = ref;

                        }}
                    />

                    <select id="CourseId" ref={(ref) => {
                        this.professor_id = ref;
                    }}>
                        {this.professor.show_all_professors.map(profesor => {
                            return <option key={profesor[1]} value={profesor[0]}>{profesor[1]} {profesor[2]}</option>
                        })}
                    </select>
                    <button type={"submit"}>add Professor</button>
                </form>}
            </div>
        );
    }
}

export default AddICourse;