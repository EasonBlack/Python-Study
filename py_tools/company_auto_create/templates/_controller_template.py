from jinja2 import Template

controller_template =  Template('''

@Singleton
class {{entityName}}Controller @Inject()(cacheApi: SyncCacheApi, {{entityName2}}Service: {{entityName}}Service,
                                     hqFeatureHelper: HqFeatureHelper, authAction: AuthAction)
                                    (implicit exec: ExecutionContext) extends BaseController {


  def view = Action { request =>
    Ok(views.html.{{entityName2}}(request.authToken, request.queryString + ("tag" -> ""),
      hqFeatureHelper.get(request.authToken.body.hqId)))
  }

  def search{{entityName}} = Action.async { request =>
    val hqId = request.authToken.body.hqId;
    {{entityName2}}Service.search{{entityName}}(hqId).map(result => dataResult(Json.toJson(result)))
  }

  def find{{entityName}}ById(id: Long) = Action.async {request =>
    val hqId = request.authToken.body.hqId
    {{entityName2}}Service.find{{entityName}}ById(hqId, id).map { result =>
      dataResult(Json.toJson(result))
    }
  }

  def save{{entityName}} = Action.async(parse.json) { request =>
    request.body.validate[{{entityName}}].fold(
      errors => Future.successful(jsonInvalidResult(request, errors)),
      m => {
        {{entityName2}}Service.save{{entityName}}(m).map(id => dataResult(JsNumber(id)))
      }
    )
  }

  def update{{entityName}} = Action.async(parse.json) { request =>
    request.body.validate[{{entityName}}].fold(
      errors => Future.successful(jsonInvalidResult(request, errors)),
      m => {
        {{entityName2}}Service.update{{entityName}}(m).map(_ => emptyResult)
      }
    )
  }

  override def Action = authAction()
}
''')