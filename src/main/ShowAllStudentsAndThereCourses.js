import React from "react";
import {observer} from "mobx-react";


@observer
class ShowAllStudentsAndThereCourses extends React.Component {
    render() {
        return <div className={"item-list"}>
            <table>
                <thead>
                <tr>
                    <th>First name</th>
                    <th>Last name</th>
                    <th>Courses</th>
                    <th>Delete Student</th>
                </tr>
                </thead>
                <tbody>
                {this.props.studentsAndCourses.show_all_Students_and_there_courses.map((professor) => {
                    return <tr key={`data=${professor[0]}`}>
                        <td>{professor[1]}</td>
                        <td>{professor[2]}</td>
                        <td>{professor[5]}</td>
                        <td>
                            <button onClick={() => {this.props.delStudent(professor[0])}}>DELETE</button>
                        </td>
                    </tr>


                })}
                </tbody>
            </table>
        </div>
    }
}

export default ShowAllStudentsAndThereCourses;