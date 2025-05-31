{{- define "secure-password-api.name" -}}
secure-password-api
{{- end }}

{{- define "secure-password-api.fullname" -}}
{{ include "secure-password-api.name" . }}
{{- end }}