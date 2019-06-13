import * as _ from 'lodash';
import * as React from 'react';
import { LinkContainer } from 'react-router-bootstrap';

import * as actions from '../../actions/notebooks';
import { isDone } from '../../constants/statuses';
import { BookmarkInterface } from '../../interfaces/bookmarks';
import { NotebookModel } from '../../models/notebook';
import { getBuildUrl, getNotebookApiUrl, splitUniqueName } from '../../urls/utils';
import { getBookmark } from '../../utils/bookmarks';
import BookmarkStar from '../bookmarkStar';
import Description from '../description';
import BackendMetaInfo from '../metaInfo/backendMetaInfo';
import BuildLinkMetaInfo from '../metaInfo/buildLinkMetaInfo';
import DatesMetaInfo from '../metaInfo/datesMetaInfo';
import IdMetaInfo from '../metaInfo/idMetaInfo';
import NodeMetaInfo from '../metaInfo/nodeMetaInfo';
import NotebookTargetMetaInfo from '../metaInfo/notebookTargetMetaInfo';
import PodIdMetaInfo from '../metaInfo/podIdMetaInfo';
import TaskRunMetaInfo from '../metaInfo/taskRunMetaInfo';
import UserMetaInfo from '../metaInfo/userMetaInfo';
import Status from '../statuses/status';
import Tags from '../tags/tags';
import NotebookActions from './notebookActions';

export interface Props {
  notebook: NotebookModel;
  onDelete: () => actions.NotebookAction;
  onStop: () => actions.NotebookAction;
  onArchive: () => actions.NotebookAction;
  onRestore: () => actions.NotebookAction;
  showBookmarks: boolean;
  bookmark: () => actions.NotebookAction;
  unbookmark: () => actions.NotebookAction;
}

function Tensorboard({
                 notebook,
                 onDelete,
                 onStop,
                 onArchive,
                 onRestore,
                 bookmark,
                 unbookmark,
                 showBookmarks
               }: Props) {
  const values = splitUniqueName(notebook.project);
  let buildUrl = '';
  let buildValues: string[] = [];
  if (!_.isNil(notebook.build_job)) {
    buildValues = splitUniqueName(notebook.build_job);
    buildUrl = getBuildUrl(buildValues[0], buildValues[1], buildValues[3]);
  }
  const bookmarkStar: BookmarkInterface = getBookmark(
    notebook.bookmarked, bookmark, unbookmark);

  return (
    <tr className="list-item">
      <td className="block">
        <Status status={notebook.last_status}/>
      </td>
      <td className="block">
        <LinkContainer to={getNotebookApiUrl(values[0], values[1], notebook.id)}>
          <a className="title">
            <i className="fa fa-gavel icon" aria-hidden="true"/>
            {notebook.name || notebook.unique_name}
          </a>
        </LinkContainer>
        {showBookmarks &&
        <BookmarkStar active={bookmarkStar.active} callback={bookmarkStar.callback}/>
        }
        <Description description={notebook.description}/>
        <div className="meta">
          <PodIdMetaInfo value={notebook.pod_id} inline={true}/>
        </div>
        <div className="meta">
          <NodeMetaInfo node={notebook.node_scheduled} inline={true}/>
        </div>
        <div className="meta">
          <IdMetaInfo value={notebook.id} inline={true}/>
          <UserMetaInfo user={notebook.user} inline={true}/>
          <DatesMetaInfo
            createdAt={notebook.created_at}
            updatedAt={notebook.updated_at}
            inline={true}
          />
        </div>
        <Tags tags={notebook.tags}/>
      </td>
      <td className="block">
        <BackendMetaInfo value={notebook.backend}/>
        <BuildLinkMetaInfo
          value={buildValues[3]}
          link={buildUrl}
        />
        <NotebookTargetMetaInfo project={notebook.project}/>
      </td>
      <td className="block">
        <TaskRunMetaInfo startedAt={notebook.started_at} finishedAt={notebook.finished_at}/>
      </td>
      <td className="block pull-right">
        <NotebookActions
          onDelete={onDelete}
          onStop={onStop}
          onArchive={notebook.deleted ? undefined : onArchive}
          onRestore={notebook.deleted ? onRestore : undefined}
          isRunning={!isDone(notebook.last_status)}
          pullRight={false}
        />
      </td>
    </tr>
  );
}

export default Tensorboard;
