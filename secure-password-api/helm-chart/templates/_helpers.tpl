{{/*
Return the full name of the chart
*/}}
{{- define "secure-password-api.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}
