import React from "react";
import {observer} from "mobx-react";
import {observable} from "mobx";


@observer
class AddTitle extends React.Component {
    @observable showForm = false;
    @observable title = null;

    render() {
        return (
            <div>
                <button onClick={(e) => {
                    this.showForm = !this.showForm

                }}>Show Add Title
                </button>
                {this.showForm &&
                <form
                    onSubmit={(event) => {
                        event.preventDefault();
                        if (!(this.title_name.value)) {
                            alert("Need title name!!!")
                            return false
                        }
                        this.props.addTitle({
                            title_name: this.title_name.value,

                        });
                        this.showForm = false;
                        this.title_name.value = "";
                    }}>

                    <input
                        placeholder={"title name"}
                        ref={(ref) => {
                            this.title_name = ref;

                        }}
                    />
                    <button type={"submit"}>add title</button>
                </form>}
            </div>
        );
    }
}

export default AddTitle;
