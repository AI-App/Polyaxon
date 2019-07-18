import * as _ from 'lodash';
import * as React from 'react';

import * as actions from '../../actions/projects';
import ActivityLogs from '../../containers/activityLogs';
import Builds from '../../containers/builds/builds';
import Experiments from '../../containers/experiments/experiments';
import Groups from '../../containers/groups/groups';
import Jobs from '../../containers/jobs/jobs';
import Notebooks from '../../containers/notebooks/notebooks';
import ProjectOverview from '../../containers/projects/projectOverview';
import Tensorboards from '../../containers/tensorboards/tensorboards';
import { BookmarkInterface } from '../../interfaces/bookmarks';
import { ProjectModel } from '../../models/project';
import { getProjectUrl, getUserUrl } from '../../urls/utils';
import { getBookmark } from '../../utils/bookmarks';
import Breadcrumb from '../breadcrumb';
import { EmptyList } from '../empty/emptyList';
import ProjectInstructions from '../instructions/projectInstructions';
import LinkedTab from '../linkedTab';
import ProjectActions from './projectActions';
import ProjectAdd from './projectAdd';

export interface Props {
  project: ProjectModel;
  onDelete: () => actions.ProjectAction;
  onArchive: () => actions.ProjectAction;
  onRestore: () => actions.ProjectAction;
  fetchData: () => actions.ProjectAction;
  bookmark: () => actions.ProjectAction;
  unbookmark: () => actions.ProjectAction;
  stopNotebook: () => actions.ProjectAction;
  stopTensorboard: () => actions.ProjectAction;
}

export default class ProjectDetail extends React.Component<Props, {}> {
  public componentDidMount() {
    this.props.fetchData();
  }

  public render() {
    const project = this.props.project;
    if (_.isNil(project)) {
      return EmptyList(false, 'project', 'project');
    }

    const bookmark: BookmarkInterface = getBookmark(
      this.props.project.bookmarked, this.props.bookmark, this.props.unbookmark);
    const projectUrl = getProjectUrl(project.user, project.name);

    return (
      <div className="row">
        <div className="col-md-12">
          <Breadcrumb
            icon="fas fa-server"
            links={[
              {name: project.user, value: getUserUrl(project.user)},
              {name: project.name}]}
            bookmark={bookmark}
            addActions={<ProjectAdd user={project.user} projectName={project.name}/>}
            actions={
              <ProjectActions
                projectName={project.name}
                onDelete={this.props.onDelete}
                onArchive={project.deleted ? undefined : this.props.onArchive}
                onRestore={project.deleted ? this.props.onRestore : undefined}
                notebookActionCallback={
                  project.has_notebook ? this.props.stopNotebook : undefined}
                tensorboardActionCallback={
                  project.has_tensorboard ? this.props.stopTensorboard : undefined}
                hasNotebook={project.has_notebook}
                hasTensorboard={project.has_tensorboard}
                pullRight={true}
              />
            }
          />
          <LinkedTab
            baseUrl={projectUrl}
            tabs={[
              {
                title: 'Overview',
                component: <ProjectOverview project={project}/>,
                relUrl: ''
              }, {
                title: 'Experiments',
                component: <Experiments
                  user={project.user}
                  projectName={project.unique_name}
                  showBookmarks={true}
                  useCheckbox={true}
                  useFilters={true}
                />,
                relUrl: 'experiments'
              }, {
                title: 'Experiment groups',
                component: <Groups
                  user={project.user}
                  projectName={project.unique_name}
                  showBookmarks={true}
                  useFilters={true}
                />,
                relUrl: 'groups'
              }, {
                title: 'Jobs',
                component: <Jobs
                  user={project.user}
                  projectName={project.unique_name}
                  showBookmarks={true}
                  useFilters={true}
                />,
                relUrl: 'jobs'
              }, {
                title: 'Builds',
                component: <Builds
                  user={project.user}
                  projectName={project.unique_name}
                  showBookmarks={true}
                  useFilters={true}
                />,
                relUrl: 'builds'
              }, {
                title: 'Tensorboards',
                component: <Tensorboards
                  user={project.user}
                  projectName={project.unique_name}
                  showBookmarks={true}
                  useFilters={true}
                />,
                relUrl: 'tensorboards'
              }, {
                title: 'Notebooks',
                component: <Notebooks
                  user={project.user}
                  projectName={project.unique_name}
                  showBookmarks={true}
                  useFilters={true}
                />,
                relUrl: 'notebooks'
              }, {
                title: 'Activity logs',
                component: <ActivityLogs user={project.user} projectName={project.name}/>,
                relUrl: 'activitylogs'
              }, {
                title: 'Instructions',
                component: <ProjectInstructions projectName={project.unique_name}/>,
                relUrl: 'instructions'
              }
            ]}
          />
        </div>
      </div>
    );
  }
}
