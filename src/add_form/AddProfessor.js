import React from "react";
import {observer} from "mobx-react";
import {observable} from "mobx";


@observer
class AddProfessor extends React.Component {
    @observable showForm = false;
    @observable title = null;

    render() {
        return (
            <div>
                <button onClick={(e) => {
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
                            this.showForm = !this.showForm;
                        })
                        .catch((error) => {
                            console.error("Error:", error);
                        });


                }}>Show Add Professors
                </button>
                {this.showForm &&
                <form
                    onSubmit={(event) => {
                        event.preventDefault();
                        if (!(this.first_name.value && this.last_name.value)) {
                            alert("Need first & last names & title!!!")
                            return false
                        }
                        this.props.addProfessor({
                            first_name: this.first_name.value,
                            last_name: this.last_name.value,
                            title_id: this.title_id.value
                        });
                        this.first_name.value = "";
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

                    <select id="title_id" ref={(ref) => {
                        this.title_id = ref;
                    }}>
                        {this.title.show_all_titles.map(title => {
                            return <option key={title[1]} value={title[0]}>{title[1]}</option>
                        })}
                    </select>
                    <button type={"submit"}>Add Professor</button>
                </form>}
            </div>
        );
    }
}

export default AddProfessor;