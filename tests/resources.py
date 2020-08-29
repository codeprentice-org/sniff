"""
This module contains a files dictionary which tracks all the test files
that are used and functions that returns resources from them according
to tags.
"""

import os
from sniffpy.mimetype import parse_mime_type

files_metadata = [
    {
        'path': "audio/aiff.aif",
        'expected_mime_type': "audio/aiff",
        'tags': ["audio"]
    },
    {
        'path': "audio/midi.mid",
        'expected_mime_type': "audio/midi",
        'tags': ["audio"]

    },
    {
        'path': "audio/mpeg.mp3",
        'expected_mime_type': "audio/mpeg",
        'tags': ["audio"]
    },
    {
        'path': "audio/wave.wav",
        'expected_mime_type': "audio/wave",
        'tags': ["audio"]
    },
    {
        'path': "image/sample_image.gif",
        'expected_mime_type': "image/gif",
        'tags': ["image"]
    },
    {
        'path': "image/sample_image.jpeg",
        'expected_mime_type': "image/jpeg",
        'tags': ["image"]
    },
    {
        'path': "image/sample_image.png",
        'expected_mime_type': "image/png",
        'tags': ["image"]
    },
    {
        'path': "video/avi.avi",
        'expected_mime_type': "video/avi",
        'tags': ["video"]
    },
    {
        'path': "video/mp4.mp4",
        'expected_mime_type': "video/mp4",
        'tags': ["video"]
    },
    {
        'path': "video/webm.webm",
        'expected_mime_type': "video/webm",
        'tags': ["video"]
    }
]


TEST_FILES_PATH = os.path.dirname(os.path.realpath(__file__))
TEST_FILES_PATH = os.path.join(TEST_FILES_PATH, 'test_files')

def filter_files_metadata(tags):
    """
    Filters the files_metadata list by the tags - if any of the
    a file metadata is filtered only if none of the tags matches
    """

    if tags:
        filtered_metadata = []
        for metadata in files_metadata:
            match = False
            for tag in tags:
                if tag in metadata['tags']:
                    match = True
            if match:
                filtered_metadata.append(metadata)
        return filtered_metadata
    return files_metadata

def get_resource_test_list(tags):
    """
    Returns test parameters for @pytest.mark.parameterize 
    so that it can check whether the relevant method can discern
    the actual MIME type of the resource. Only the relevant test
    parameters are returned according to the tags from the 
    files_metadata. Also reads from test_files directory to get
    the relevant resources.
    """

    filtered_files_metadata = filter_files_metadata(tags)
    resources = []
    for metadata in filtered_files_metadata:
        file_path = os.path.join(TEST_FILES_PATH, metadata['path'])
        expected_mime_type = parse_mime_type(metadata['expected_mime_type'])
        with open(file_path, "rb") as f:
            resource = f.read()
            resources.append((expected_mime_type, resource))
    return resources
