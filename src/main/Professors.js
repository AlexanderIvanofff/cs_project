import React from "react";
import {observer} from "mobx-react";


@observer
class Professors extends React.Component {
    render() {
        return <div className={"item-list"}>
            <table>
                <thead>
                <tr>
                    <th>First name</th>
                    <th>Last name</th>
                    <th>Delete professor</th>
                </tr>
                </thead>
                <tbody>
                {this.props.show_all_professors.show_all_professors.map((professor) => {
                    return <tr key={`data=${professor[0]}`}>
                        <td>{professor[1]}</td>
                        <td>{professor[2]}</td>
                        <td><button onClick={() => {
                                this.props.deleteProfessor(professor[0])}}>DELETE
                            </button>
                        </td>
                    </tr>

                })}
                </tbody>
            </table>
        </div>
    }
}

export default Professors;