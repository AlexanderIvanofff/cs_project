import React from "react";
import {observer} from "mobx-react";


@observer
class ShowThreeTopCourses extends React.Component {
    render() {
        return <div className={"item-list"}>
            <table>
                <thead>
                <tr>
                    <th>Courses</th>
                    <th>Student Count</th>
                </tr>
                </thead>
                <tbody>
                {this.props.showTopThreeCourses.show_top_three_courses.map((course) => {
                    return <tr key={`data=${course[0]}`}>
                        <td>{course[0]}</td>
                        <td>{course[1]}</td>
                    </tr>

                })}
                </tbody>
            </table>
        </div>
    }
}

export default ShowThreeTopCourses;