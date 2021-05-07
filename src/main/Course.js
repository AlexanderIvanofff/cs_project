import React from "react";
import {observer} from "mobx-react";


@observer
class Course extends React.Component {
    render() {
        return <div className={"item-list"}>
            <table>
                <thead>
                <tr>
                    <th>Course Name</th>
                    <th>Credits</th>
                    <th>Delete Course</th>
                </tr>
                </thead>
                <tbody>
                {this.props.courses.show_all_courses.map((course) => {
                    return <tr key={`data=${course[0]}`}>
                        <td>{course[1]}</td>
                        <td>{course[2]}</td>
                        <td><button onClick={() => {
                            this.props.delCourse(course[0])}}>DELETE
                        </button>
                        </td>
                    </tr>

                })}
                </tbody>
            </table>
        </div>
    }
}

export default Course;