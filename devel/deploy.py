from common.names import fn_deployment
from configure.settings import app_config
from pathlib import Path
import os
import shutil
import yaml

source_project = app_config['path'].project
projects = app_config['path'].children['projects']

# inventory of links to be created
links_to_create = dict(app_config['deployment']['link at target'])
files_to_copy = dict(app_config['deployment']['copy to target'])

# search projects for existence of ./setting/deployment.yaml
deployment_details = dict()
for project, project_path in projects.items():
    path_to_deployment_config = Path(project_path, 'setting', fn_deployment)
    if project_path == source_project:
        continue  # skip self
    if os.path.exists(path_to_deployment_config):
        with open(path_to_deployment_config, 'r') as d_cfg:
            deployment_config = yaml.safe_load(d_cfg)
        deployment_details.update({project_path: deployment_config['receive']})

# build and deploy the links
for link_label, link_parts in links_to_create.items():
    deploy = True
    deployment_path = None
    for deployment_path, deployment_elements in deployment_details.items():
        deploy = True if link_label in deployment_elements else False
    if not deploy or not deployment_path:
        continue
    # make the parent directory if needed
    target_dir = Path(deployment_path, link_parts[0])
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    source_file = Path(source_project, * link_parts)
    target_file = Path(deployment_path, * link_parts)
    if not os.path.exists(target_file) and app_config['deployment'].get('mode') != 'delete':
        # execute the creation
        os.symlink(src=source_file, dst=target_file)
        continue
    if app_config['deployment']['mode'] == 'delete' and Path(target_file).is_symlink():
        os.remove(path=target_file)


# build and copy the unlinked files
for copy_label, copy_parts in files_to_copy.items():
    deploy = True
    deployment_path = None
    for deployment_path, deployment_elements in deployment_details.items():
        deploy = True if copy_label in deployment_elements else False
    if not deploy or not deployment_path:
        continue
    # make the parent directory if needed
    target_dir = Path(deployment_path, copy_parts[0])
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    source_file = Path(source_project, * copy_parts)
    target_file = Path(deployment_path, * copy_parts)
    if not os.path.exists(target_file):
        # execute the creation
        shutil.copy(src=source_file, dst=target_file)

print(f'link deployment complete')
