import React from "react";
import {observer} from "mobx-react";


@observer
class ShowProfessorsAndCourses extends React.Component {
    render() {
        return <div className={"item-list"}>
            <table>
                <thead>
                <tr>
                    <th>First name</th>
                    <th>Last name</th>
                    <th>Courses</th>
                    <th>Student Count</th>
                </tr>
                </thead>
                <tbody>
                {this.props.professors.show_all_professors_and_courses.map((professor) => {
                    return <tr key={`data=${professor[0]}`}>
                        <td>{professor[1]}</td>
                        <td>{professor[2]}</td>
                        <td>{professor[5]}</td>
                        <td>{professor[12]}</td>
                    </tr>

                })}
                </tbody>
            </table>
        </div>
    }
}

export default ShowProfessorsAndCourses;

