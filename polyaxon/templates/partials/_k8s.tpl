{{/*
k8s config
*/}}
{{- define "config.k8s" }}
- name: POLYAXON_K8S_APP_NAME
  value: {{ template "polyaxon.fullname" . }}
- name: POLYAXON_K8S_API_HOST
  value: {{ template "polyaxon.fullname" . }}-api
- name: POLYAXON_K8S_API_PORT
  value: {{ .Values.api.service.externalPort | quote }}
- name: POLYAXON_K8S_APP_CONFIG_NAME
  value: {{ template "polyaxon.fullname" . }}-config
- name: POLYAXON_K8S_APP_SECRET_NAME
  value: {{ template "polyaxon.fullname" . }}-secret
- name: POLYAXON_K8S_RABBITMQ_SECRET_NAME
  value: {{ template "rabbitmq.fullname" . }}
- name: POLYAXON_K8S_DB_SECRET_NAME
{{- if .Values.postgresql.enabled }}
  value: {{ template "postgresql.fullname" . }}
{{- else }}
  value: {{ template "polyaxon.fullname" . }}-postgres-secret
{{- end}}
{{- if .Values.k8s.authorisation }}
- name: POLYAXON_K8S_AUTHORISATION
  valueFrom:
    secretKeyRef:
      name: {{ template "polyaxon.fullname" . }}-secret
      key: k8s-authorisation
{{- end }}
- name: POLYAXON_K8S_HOST
  value: {{ .Values.k8s.host | quote }}
{{- if .Values.k8s.ssl_ca_cert }}
- name: POLYAXON_K8S_SSL_CA_CERT
  value: {{ .Values.k8s.ssl_ca_cert | quote }}
{{- end }}
{{- end -}}
