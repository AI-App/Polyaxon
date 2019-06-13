import * as _ from 'lodash';
import { connect } from 'react-redux';
import { RouteComponentProps, withRouter } from 'react-router-dom';
import { Dispatch } from 'redux';

import * as codeRefActions from '../../actions/codeReference';
import * as actions from '../../actions/experiments';
import ExperimentDetail from '../../components/experiments/experimentDetail';
import { AppState } from '../../constants/types';
import { getExperimentUniqueName } from '../../urls/utils';

interface Props extends RouteComponentProps<any> {}

export function mapStateToProps(state: AppState, props: Props) {
  const experimentUniqueName = getExperimentUniqueName(
    props.match.params.user,
    props.match.params.projectName,
    props.match.params.experimentId);
  return _.includes(state.experiments.uniqueNames, experimentUniqueName) ?
    {experiment: state.experiments.byUniqueNames[experimentUniqueName]} :
    {experiment: null};
}

export interface DispatchProps {
  fetchData?: () => actions.ExperimentAction;
  onUpdate: (updateDict: { [key: string]: any }) => actions.ExperimentAction;
  onDelete: () => actions.ExperimentAction;
  onStop: () => actions.ExperimentAction;
  onArchive: () => actions.ExperimentAction;
  onRestart: () => actions.ExperimentAction;
  onRestore: () => actions.ExperimentAction;
  bookmark: () => actions.ExperimentAction;
  unbookmark: () => actions.ExperimentAction;
  stopTensorboard: () => actions.ExperimentAction;
  getCodeReference: () => codeRefActions.CodeReferenceAction;
}

export function mapDispatchToProps(dispatch: Dispatch<actions.ExperimentAction>, params: any): DispatchProps {
  return {
    fetchData: () => dispatch(
      actions.getExperiment(
        params.match.params.user,
        params.match.params.projectName,
        params.match.params.experimentId)),
    onUpdate: (updateDict: { [key: string]: any }) => dispatch(
      actions.updateExperiment(
        getExperimentUniqueName(
          params.match.params.user,
          params.match.params.projectName,
          params.match.params.experimentId),
        updateDict)),
    onDelete: () => dispatch(
      actions.deleteExperiment(
        getExperimentUniqueName(
          params.match.params.user,
          params.match.params.projectName,
          params.match.params.experimentId),
        true)),
    onStop: () => dispatch(
      actions.stopExperiment(
        getExperimentUniqueName(
          params.match.params.user,
          params.match.params.projectName,
          params.match.params.experimentId))),
    onArchive: () => dispatch(
      actions.archiveExperiment(
        getExperimentUniqueName(
          params.match.params.user,
          params.match.params.projectName,
          params.match.params.experimentId),
        true)),
     onRestart: () => dispatch(
      actions.restartExperiment(
        getExperimentUniqueName(
          params.match.params.user,
          params.match.params.projectName,
          params.match.params.experimentId),
        true)),
    onRestore: () => dispatch(
      actions.restoreExperiment(
        getExperimentUniqueName(
          params.match.params.user,
          params.match.params.projectName,
          params.match.params.experimentId))),
    bookmark: () => dispatch(
      actions.bookmark(getExperimentUniqueName(
        params.match.params.user,
        params.match.params.projectName,
        params.match.params.experimentId))),
    unbookmark: () => dispatch(
      actions.unbookmark(getExperimentUniqueName(
        params.match.params.user,
        params.match.params.projectName,
        params.match.params.experimentId))),
    getCodeReference: () => dispatch(
      actions.getExperimentCodeReference(getExperimentUniqueName(
        params.match.params.user,
        params.match.params.projectName,
        params.match.params.experimentId))),
    stopTensorboard: () => dispatch(
      actions.stopTensorboard(
        getExperimentUniqueName(
          params.match.params.user,
          params.match.params.projectName,
          params.match.params.experimentId))),
  };
}

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(ExperimentDetail));
