from common.names import fn_deployment
from configure.settings import app_config
from pathlib import Path
import os
import shutil
import yaml

source_project = app_config['path'].project
projects = app_config['path'].children['projects']

# inventory of links to be created
deployment_features = app_config['deployment']['features']
features_linked = deployment_features['linked']
features_unlinked = deployment_features['unlinked']

# search projects for existence of ./../project/setting/deployment.yaml
deployment_details = dict()
for project, project_path in projects.items():
    path_to_target_deployment = Path(project_path, 'setting', fn_deployment)
    if project_path == source_project:
        continue  # skip self
    if os.path.exists(path_to_target_deployment):
        with open(path_to_target_deployment, 'r') as d_cfg:
            deployment_config = yaml.safe_load(d_cfg)
        deployment_details.update({project_path: deployment_config['receive features']})

# build and deploy linked features
for feature, feature_components in features_linked.items():
    deploy = False
    deployment_path = None
    component_segments = None
    for deployment_path, features_to_deploy in deployment_details.items():
        for component_name, component_segments in feature_components.items():
            deploy = True if feature in features_to_deploy else False
            if not deploy or not deployment_path:
                continue
            # make the parent directory if needed
            target_parent = Path(deployment_path, component_segments[0])
            if not os.path.exists(target_parent):
                os.mkdir(target_parent)
            source_file = Path(source_project, * component_segments)
            target_file = Path(deployment_path, * component_segments)
            if not os.path.exists(target_file) and \
                    app_config['deployment'].get('mode') != 'delete':
                # execute the creation
                os.symlink(src=source_file, dst=target_file)
                continue
            if app_config['deployment']['mode'] == 'delete' \
                    and Path(target_file).is_symlink():
                os.remove(path=target_file)


# build and deploy unlinked features
for feature, feature_components in features_unlinked.items():
    deploy = False
    deployment_path = None
    component_segments = None
    for deployment_path, features_to_deploy in deployment_details.items():
        for component_name, component_segments in feature_components.items():
            deploy = True if feature in features_to_deploy else False
            if not deploy or not deployment_path:
                continue
            # make the parent directory if needed
            target_parent = Path(deployment_path, component_segments[0])
            if not os.path.exists(target_parent):
                os.mkdir(target_parent)
            source_file = Path(source_project, *component_segments)
            target_file = Path(deployment_path, *component_segments)
            if not os.path.exists(target_file) and \
                    app_config['deployment'].get('mode') != 'delete':
                # execute the creation
                shutil.copy(src=source_file, dst=target_file)
                continue

# cleanup empty directories in target projects
if app_config['deployment'].get('mode') == 'delete':
    for deployment_path in deployment_details:
        for root, directories, _ in os.walk(deployment_path):
            for directory in directories:
                project_sub_path = Path(root, directory)
                try:
                    os.rmdir(project_sub_path)
                except Exception as exc:
                    print(f'{exc}')
            break  # do not recurse

print(f'link deployment complete')
