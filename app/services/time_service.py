from datetime import datetime, timedelta


def processar_horarios(
    hora_inicio,
    hora_fim,
    duracao_minutos
):

    if hora_inicio and not hora_fim and duracao_minutos:

        inicio = datetime.strptime(
            hora_inicio,
            "%H:%M"
        )

        fim = inicio + timedelta(
            minutes=int(duracao_minutos)
        )

        hora_fim = fim.strftime("%H:%M")

    return hora_inicio, hora_fim