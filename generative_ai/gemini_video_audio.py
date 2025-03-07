# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")


def analyze_video_with_audio() -> str:
    # [START generativeaionvertexai_gemini_video_with_audio]

    import vertexai
    from vertexai.generative_models import GenerativeModel, Part

    # TODO(developer): Update project_id and location
    vertexai.init(project=PROJECT_ID, location="us-central1")

    model = GenerativeModel("gemini-1.5-flash-001")

    prompt = """
    Provide a description of the video.
    The description should also contain anything important which people say in the video.
    """

    video_file = Part.from_uri(
        uri="gs://cloud-samples-data/generative-ai/video/pixel8.mp4",
        mime_type="video/mp4",
    )

    contents = [video_file, prompt]

    response = model.generate_content(contents)
    print(response.text)

    # [END generativeaionvertexai_gemini_video_with_audio]
    return response.text
