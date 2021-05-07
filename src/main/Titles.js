import React from "react";
import {observer} from "mobx-react";


@observer
class Titles extends React.Component {
    render() {
        return <div className={"item-list"}>
            <table>
                <thead>
                <tr>
                    <th>Titles</th>
                    <th>Delete Title</th>
                </tr>
                </thead>
                <tbody>
                {this.props.title.show_all_titles.map((title) => {
                    return <tr key={`data=${title[0]}`}>
                        <td>{title[1]}</td>
                        <td>
                            <button onClick={() => {
                                this.props.delete_title(title[0])}}>DELETE
                            </button>
                        </td>
                    </tr>

                })}
                </tbody>
            </table>
        </div>
    }
}

export default Titles;