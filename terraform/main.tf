terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.62.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
  zone    = var.zone
}

# Deploy image to Cloud Run
resource "google_cloud_run_service" "youtube_object_detection_api" {
  provider = google
  name     = "youtube-object-detection-api"
  location = var.region
  template {
    spec {
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/${var.repository}/${var.docker_image}"
        resources {
          limits = {
            "memory" = "32G"
            "cpu"    = "8"
          }
        }
      }
    }
    metadata {
      annotations = {
        "autoscaling.knative.dev/minScale" = "1"
        "autoscaling.knative.dev/maxScale" = "1"
      }
    }
  }
  traffic {
    percent         = 100
    latest_revision = true
  }
}

# Create a policy that allows all users to invoke the API
data "google_iam_policy" "noauth" {
  provider = google
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

# Apply the no-authentication policy to our Cloud Run Service.
resource "google_cloud_run_service_iam_policy" "noauth" {
  provider = google
  location = var.region
  project  = var.project_id
  service  = google_cloud_run_service.youtube_object_detection_api.name

  policy_data = data.google_iam_policy.noauth.policy_data
}

output "cloud_run_instance_url" {
  value = google_cloud_run_service.youtube_object_detection_api.status.0.url
}