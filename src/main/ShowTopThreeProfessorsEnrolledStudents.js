import React from "react";
import {observer} from "mobx-react";


@observer
class ShowTopThreeProfessorsEnrolledStudents extends React.Component {
    render() {
        return <div className="Data">
            {this.props.show_top_three_professors_enrolled_students.show_top_three_professors_enrolled_students_in_courses.map((professors) => {
                return <div key={`data=${professors[0]}`}>
                    <table>
                        <thead>
                        <tr>
                            <th>first name</th>
                            <th>last name</th>
                            <th>course count</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>{professors[3]}</td>
                            <td>{professors[4]}</td>
                            <td>{professors[6]}</td>
                        </tr>
                        </tbody>
                    </table>

                </div>
            })}
        </div>
    }
}

export default ShowTopThreeProfessorsEnrolledStudents;